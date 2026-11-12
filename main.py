"""Build a plain-English world news summary for 11 November 2026.

Stdlib only. No network access, no randomness, no clock reads: the output
is a pure function of the facts embedded below, so repeated runs are
byte-identical. Writes /output/entry.txt.
"""

import os

FACTS = [
    "Zaporizhzhia mayor Regina Kharchenko spoke of constant fear of Russian attacks.",
    "NATO's DSACEUR backed Ukraine's strikes on Russian diesel infrastructure.",
    "US-convened talks on Europe's postwar security opened in Abu Dhabi.",
    "Russia's ambassador to the US, Alexander Darchiev, died aged 66.",
    "Russia barred four French figures in retaliation for RT France chief Xenia Fedorova's expulsion.",
    "Spain's first nationwide general strike since 2012 brought 120,000 to Madrid over housing, with Barcelona clashes.",
    "Portugal closed all ~8,000 schools before Storm Charles, a first in living memory.",
    "France's 108th armistice: Macron at the Arc de Triomphe, with Le Pen and Melenchon eyeing the presidential election.",
    "The EU proposed a Digital Fairness Act against subscription traps, addictive design and hidden fees.",
    "SpaceX signed a EUR 60 million solar-cell deal with Germany's Singulus.",
    "Portugal's Vangest will build parts for Saab's Gripen fighter.",
    "US inflation topped forecasts, tempering Europe's tech rally.",
    "Trinidad and Tobago's top court overturned its ban on gay sex.",
    "French journalist Christophe Gleizes marked 500 days in an Algerian prison.",
    "Several key EU leaders skipped COP31's opening.",
]

HEADER = "World news, 11 November 2026.\n\n"
FOOTER = "\n\nFrom Zaporizhzhia to Madrid to Brussels, the day showed conflict stress, civic anger and new rules colliding across Europe."

def build() -> str:
    body = "".join(fact + "\n" for fact in FACTS)
    return HEADER + body + FOOTER

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = build()
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars")

if __name__ == "__main__":
    main()
