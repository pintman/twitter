# Wie Du Dein Twitter-Archiv nutzt

Der einfachste Weg, Dein Twitter-Archiv zu nutzen, ist mit Hilfe des Archiv-Browser-Interfaces, das in dieser Datei bereitgestellt wird. Doppelklicke einfach auf `index.html` im Hauptverzeichnis, und Du kannst in Deinem Browser durch Deine gesamte Tweet-Historie blättern.

---

Im `data` Ordner ist Dein Twitter-Archiv in zwei Formaten vorhanden: JSON und CSV exportiert nach Monat und Jahr.

* CSV ist ein allgemeines Format, das in viele Daten-Tools und Tabellenkalkulations-Applikationen importiert oder einfach mit einer Programmiersprache eingelesen werden kann.

## JSON für Entwickler

* Der JSON-Export beinhaltet eine komplette Darstellung Deiner Tweets, so wie sie von der Twitter-API v1.1 zurückgegeben werden. Sieh Dir https://dev.twitter.com/docs/api/1.1 für weitere Informationen an.
* Der JSON-Export wird auch zur Bereitstellung des Archiv-Browser-Interfaces genutzt (index.html).
* Um den Export in einem gewöhnlichen JSON-Parser jeglicher Sprache einlesen zu können, müssen die erste und letzte Zeile jeder Datei entfernt werden.

Um Feedback abzugeben, Fragen zu stellen oder Ideen mit anderen Twitter-Entwicklern zu teilen, trete den Diskussionsforen auf https://dev.twitter.com bei.