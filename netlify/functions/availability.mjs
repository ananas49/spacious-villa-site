// Renvoie les nuits déjà réservées, lues dans les calendriers iCal (Airbnb, Booking, Google Agenda).
// Les liens sont stockés dans la variable d'environnement Netlify ICAL_URLS (séparés par des espaces ou des virgules).
// Réponse : { "booked": ["2026-12-01", ...] } — une date = une nuit occupée.

const DAY = 86400000;

function unfold(text) {
  return text.replace(/\r?\n[ \t]/g, "");
}

function toIso(value) {
  const m = /^(\d{4})(\d{2})(\d{2})/.exec(value.trim());
  return m ? `${m[1]}-${m[2]}-${m[3]}` : null;
}

export function parseIcal(text) {
  const nights = new Set();
  const lines = unfold(text).split(/\r?\n/);
  let start = null, end = null, inEvent = false;
  for (const line of lines) {
    if (line.startsWith("BEGIN:VEVENT")) { inEvent = true; start = end = null; continue; }
    if (line.startsWith("END:VEVENT")) {
      if (inEvent && start) {
        const s = Date.parse(start + "T00:00:00Z");
        const e = end ? Date.parse(end + "T00:00:00Z") : s + DAY;
        for (let t = s; t < e && t - s < 400 * DAY; t += DAY) {
          nights.add(new Date(t).toISOString().slice(0, 10));
        }
      }
      inEvent = false; continue;
    }
    if (!inEvent) continue;
    const i = line.indexOf(":");
    if (i < 0) continue;
    const key = line.slice(0, i).split(";")[0].toUpperCase();
    if (key === "DTSTART") start = toIso(line.slice(i + 1));
    if (key === "DTEND") end = toIso(line.slice(i + 1));
  }
  return nights;
}

export default async () => {
  const raw = (globalThis.Netlify?.env?.get("ICAL_URLS") ?? process.env.ICAL_URLS ?? "").trim();
  const urls = raw.split(/[\s,]+/).filter((u) => /^https:\/\//.test(u));
  const today = new Date().toISOString().slice(0, 10);
  const booked = new Set();
  let ok = 0;
  await Promise.all(urls.map(async (url) => {
    try {
      const res = await fetch(url, { headers: { "User-Agent": "SpaciousVilla-availability/1.0" } });
      if (!res.ok) return;
      for (const d of parseIcal(await res.text())) if (d >= today) booked.add(d);
      ok++;
    } catch (_) { /* calendrier injoignable : on l'ignore */ }
  }));
  const body = JSON.stringify({ booked: [...booked].sort(), sources: ok, configured: urls.length > 0 });
  return new Response(body, {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "public, max-age=0, must-revalidate",
      "Netlify-CDN-Cache-Control": "public, s-maxage=900, stale-while-revalidate=3600",
    },
  });
};

export const config = { path: "/api/availability" };
