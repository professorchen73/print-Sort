# printSort
## Was tut es?
Es zeigt visuell die Funktion eines Sortieralgorithmuses in der Konsole. Die Zahlen werden zufällig genertiert.
<img src="example.png" width="500">
- **Rot**: Erste Schleife; Wird verglichen mit:
- **Gelb**: Zweite Schleife
- **Grün**: Makiert die aktuell kleinste Zahl in der zweiten Schleife

## Use
> :warning: **nur für Linux/macOS Terminals**
```
python3 printSort.py <länge> <maximal> <sleep>
```
- `<länge>`: `int` Wie viele Zahlen sollen sortiert/generiert werden?
- `<maximal>`: `int` Wie groß soll die größte Zahl sein?
- (optional) `<sleep>`: `float` wie lange soll eine Änderung angezeigt werden? (default: `0.2`)
