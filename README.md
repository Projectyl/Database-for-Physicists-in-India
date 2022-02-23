# **𝒟βπ**

𝒟βπ (*D*ata*b*ase for *P*hysicists in *I*ndia) is a set of python scripts designed to create a database of details for physicists working in India. The database is created by crawling through the websites of various institutes. This is part of our efforts, in the form of [Projectyl](https://projectyl.github.io/), to disseminate information towards internships and short-term projects (of physics) in India as a stepping-stone for a career in research. The data gathered is then displayed on the Projectyl website.

## Structure of Database

The database is essentially stored in category_data, in the form of JSON files. Each file represents a broad category in physics like optics or high energy physics, and contains information of physicists working in that particular category. The information for a typical physicist is of the form:

| Name | Institute | Designation | Interests | Webpage | Email Id |
| :---:  | :---: | :---: | :---: | :---: | :---: |
| Armin Arlert | Indian Institute for ODM Study | Assistant Professor | Gamma ray spectroscopy, nuclear weapons | https://iios.ac.in/aa/ | aa@iios.ac.in |

## Details of the Information Files

There are several information files in the info_files folder. They acts as global repositories of information that are used by multiple scripts.

- [category_file.json](info_files/category_file.json): Usually physicists will not use broad categories while describing their interests; they use more specific terms. This file groups the specific terms into the broader terms, such that the physicists themselves can then be classified into broad categories depending on their interests.

- [grouped_tags.json](info_files/grouped_tags.json): This lists all the specific terms that have *already* been grouped into the broader categories.

- [headings.json](info_files/headings.json): This lists the headers for the scientists database; these are the headers that appear in the table of the [Structure of Database section](#structure-of-database).

- [institutes.json](info_files/institutes.json): This lists the institutes currently being scraped through.

- [ungrouped_tags.json](info_files/ungrouped_tags.json): This lists all the specific terms that have *not yet* been grouped into the broader categories.

## Institute Retrievers and Institute Data

The folder institute_retrievers contains the code that scrapes and gathers data from the websites. Each institute has a separate script. The data for each institute is stored in its own file in the institute_data folder.

## List of Sources Implemented

| Source | Status | Comments |
| :---:  | :---: | :---: |
| IISER-K | :heavy_check_mark: | - | 
| IIT-KGP | :heavy_check_mark: | - | 

