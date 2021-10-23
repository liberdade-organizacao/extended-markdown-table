# Extended Markdown Table

This is an idea for a extension of Markdown tables so they may be (kinda)
used as spreadsheets.

Markdown tables currently look like this:

``` markdown
| name   | age | job       |
|--------|-----|-----------|
| Mira   | 27  | Superhero |
| Pietro | 24  | Clown     |
| Flora  | 18  | Singer    |
```

The idea is to include more lines below the table describing new columns
that will be calculated using a provided formula using whatever programming
language is best suited.

The extension lines will start with a colon `:`, followed by the new
column name, followed by an equals sign `=`, and finally the equation for this
new column.

An example of the proposed syntax is the following with Javascript as
scripting language:

``` markdown
| name   | age | job       |
|--------|-----|-----------|
| Mira   | 27  | Superhero |
| Pietro | 24  | Clown     |
| Flora  | 18  | Singer    |
: title = (t, r, i) => `${r["name"]}, the ${r["job"]}`
```

This should create a new column called `filled` using the function as a rule.
This function should have 3 parameters: `t` is the whole table, `r` is the
current row, and `i` is the index of the current row.

Extending this table should yield this result:

``` markdown
| name   | age | job       | title               |
|--------|-----|-----------|---------------------|
| Mira   | 27  | Superhero | Mira, the Superhero |
| Pietro | 24  | Clown     | Pietro, the Clown   |
| Flora  | 18  | Singer    | Flora, the Singer   |
```

This same syntax could work, for example, with Python:

``` markdown
| name   | age | job       |
|--------|-----|-----------|
| Mira   | 27  | Superhero |
| Pietro | 24  | Clown     |
| Flora  | 18  | Singer    |
: title = lambda t, r, i: "{}, the {}".format(r["name"], r["job"])
```

The idea is to keep this language agnostic so the designers can use
the best language depending on the situation.
