## Scientists Database Creator

- The intention is to crawl through various website to create a database of (Indian) scientists working in physics and related fields

- Results will be stored in the following structure

```
project root
|
│   code.ipynb
|
└───database folder
        |
        │   high_energy_physics.csv
        |
        │   strongly_correlated_electrons.csv
        |
        │   quantum_magnetism.csv
        |
        |   low_dimensional_materials.csv
```


- Websites to crawl include google scholar and those of institutes like the IITs, IISERs, etc.

- The code will be structured in the form of separate modules for each website.
- Each module outputs results in a common format. This common format will be a dictionary, of the form

`results={'complex_networks':[[Name 1, Affil 1, Webpage 1, Interests 1], [Name 2, Affil 2, Webpage 2, Interests 2]], 'quantum_magnetism':[[...]]}`

- In other words, the keys of the dictionary are the interests, and the data of each key is a list. This list is itself formed by several lists, each of these smaller lists giving the information for a particular scientist. 

- Only the information of those scientits who have that particular interest will enter that particular key.

- As an example, lets say the results are as follows. Scientist A1 with affiliation B1 has interests X1 and X2, while scientist A2 with affiliation B2 has interests X2 and X3. Then, the complete dictionary is `results={X1: [[A1, B1, "X1, X2"]], X2: [[A1, B1, "X1, X2"],[A2, B2, "X2, X3"]], X3: [[A2, B2, "X2, X3"]]}`

- Each of these separate keys will be written to individual files, `X1.csv, X2.csv` and so on. 

- In each file, the first row will have the headers "Name, Affiliation", etc, and each of the subsequent rows will consist of the details of the scientists. Each scientist will occupy one complete row.

- The delimiter has been chosen to be `'\t'`, because comma is pretty common in the text.
