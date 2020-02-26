# Create CLI to generate and read data using Python and SQLite

This instruction will guide how to use this CLI (Command Line Interface) to generate and read data using SQLite.

## Background

### Why SQLite?

Before we come so far, I was at first having some options to store data at:
* JSON
* CSV
* Parquet (actually not sure for this, because never tried, but there's always first time for everything)
I am facing problem that can come with so much records and should be able to access by using filtering. I am wondering using either CSV or JSON will be able to read data using filtering. Because it will give pain to handle that. Then SQLite became my choice since it's just like common RDB. I have no idea actually about how large the file will be since I only generate 10000 data and the size is 1.2MB. I am wondering actually if we compare it to JSON or CSV. But in performance, I think SQLite will be the best since we can create index in it. So, although the data increases, the performance will still remain.

## Prerequisites

Before we can run this, we should install Python. I am using Python 3.7.6 as interpreter and Miniconda to create virtual environment. If we only use Python in-built virtual environment, we can just install the modules that I already provided in requirement.txt using pip command.

```
pip install -r requirement.txt
```

If we use Miniconda, then we can create the virtual environment using requirement.yml file using conda command.

```
conda env create -f requirement.yml
```

## Guidelines

### Step 1

First thing first, we need to complete all the prerequisites above. What to do next is activate virtual environment or if we don't use virtual environment, the requirements must be installed.

### Step 2

We should generate data first before able to read data.

```
python ./main_generate.py N
```

The example to generate 10000 records of data:

```
python ./main_generate.py 10000
```

N is positional argument that must be included while running the command. It determines how much the data will be generated. Then it will create a db file named efishery.db that where the data we generate store at.

### Step 3

After generating data, we can directly access the data. Commands that can be run to access the data will be like below.

```
python ./main_read.py --show X              --> X will be either asc or desc. asc is to show first hundred data while desc is to show last hundred data
python ./main_read.py -- filter X X         --> The X's will be 'filter_by' type in between (all, device_id, username, lokasi, and timerange) and value respectively to filter data
python ./main_read.py --nrow NROW           --> The NROW is an integer which represents data that stores with that order
python ./main_read.py --max {all,device_id,username,lokasi}           --> To show max number of amount with group type
python ./main_read.py --min {all,device_id,username,lokasi}           --> To show min number of amount with group type
python ./main_read.py --avg {all,device_id,username,lokasi}           --> To show average number of amount with group type
python ./main_read.py --sum {all,device_id,username,lokasi}           --> To show sum number of amount with group type
python ./main_read.py --count {all,device_id,username,lokasi}           --> To show count number of amount with group type
```

It will print out the result into the console in table format.

## Notes

* For timerange in filter command, actually it's not supposed to be using one time format. It should be using two time format.