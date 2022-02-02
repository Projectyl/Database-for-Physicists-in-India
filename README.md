# Scientists Database Creator

## What's the Big Idea?

The python programs will crawl through the listed Indian institutes websites and collect information about the scientists working in physics and other related fields. The data will be classified according to research topics of the scientists, and then made available through a website. Viewers will then be able to find the list of Indian scientists working in a particular field like, say, high energy physics.

## List of Sources Implemented

| Source | Status | Comments |
| :---:  | :---: | :---: |
| IISER-K | :heavy_check_mark: | | 
| Google Scholar | :heavy_check_mark: | |
| IISc | :triangular_flag_on_post: | |

## Details of the algorithm

- Files will be stored in the following structure

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

- The code will be structured in the form of separate modules for each website.

- **Each module outputs results in a common format. This common format will be a dictionary, of the form**

`results={'complex_networks':[[Name 1, Institute 1, Designation 1, Webpage 1, Interests 1], [Name 2, Institute 2, Designation 2, Webpage 2, Interests 2]], 'quantum_magnetism':[[...]]}`

- In other words, the keys of the dictionary are the interests, and the data of each key is a list. This list is itself formed by several lists, each of these smaller lists giving the information for a particular scientist. 

- Only the information of those scientits who have that particular interest will enter that particular key.

- As an example, lets say the results are as follows. Scientist A1 with designation B1 has interests X1 and X2, while scientist A2 with designation B2 has interests X2 and Xe. Then, the complete dictionary is `results={X1: [[A1, B1, "X1, X2"]], X2: [[A1, B1, "X1, X2"],[A2, B2, "X2, X3"]], X3: [[A2, B2, "X2, X3"]]}`

- Each of these separate keys will be written to individual files, `X1.csv, X2.csv` and so on. 

- In each file, the first row will have the headers "Name, Affiliation", etc, and each of the subsequent rows will consist of the details of the scientists. Each scientist will occupy one complete row.

- The delimiter has been chosen to be `'\t'`, because comma is pretty common in the text.
