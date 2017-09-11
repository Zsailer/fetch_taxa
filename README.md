# fetch_taxon

A simple python package to fetch taxonomic data through Entrez.

## Basic Example

Simply read some csv file with a list of accession numbers.

**Bash command**
```bash
fetch_taxa -i accession_list.csv -o taxa_data.csv --email "myemail@gmail.com"
```

**accession_list.csv**

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>accver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WP_051844355</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WP_018794778</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WP_030812438</td>
    </tr>
    <tr>
      <th>3</th>
      <td>EPH42135</td>
    </tr>
    <tr>
      <th>4</th>
      <td>EXG79206</td>
    </tr>
    <tr>
      <th>5</th>
      <td>WP_019676482</td>
    </tr>
  </tbody>
</table>

**taxa_data.csv**

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>accver</th>
      <th>defline</th>
      <th>gi</th>
      <th>length</th>
      <th>orgname</th>
      <th>seqtype</th>
      <th>sequence</th>
      <th>sid</th>
      <th>taxid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>WP_051844355.1</td>
      <td>streptogrisin [Streptomyces sp. NRRL S-813]</td>
      <td>917237643</td>
      <td>292</td>
      <td>Streptomyces sp. NRRL S-813</td>
      <td>None</td>
      <td>MLTPEEAVLRFKRTTFATAIASALIAAGALAGPAQAAPSPAQQAKS...</td>
      <td>NaN</td>
      <td>1463919</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>WP_018794778.1</td>
      <td>S1 family peptidase [Salinispora arenicola]</td>
      <td>517624570</td>
      <td>346</td>
      <td>Salinispora arenicola</td>
      <td>None</td>
      <td>MRPTRSLLCRAASLAAVGALVAGTLSSAPAQASPAPATPEVAASLS...</td>
      <td>NaN</td>
      <td>168697</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>WP_030812438.1</td>
      <td>S1 family peptidase [Streptomyces sp. NRRL F-2...</td>
      <td>664282314</td>
      <td>300</td>
      <td>Streptomyces sp. NRRL F-2799</td>
      <td>None</td>
      <td>MRIKRTTHRGRIARRTQLAAAVSGLLAVAAFAAPTANASDVHTFSA...</td>
      <td>NaN</td>
      <td>1463844</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>EPH42135.1</td>
      <td>putative Streptogrisin-D [Streptomyces auranti...</td>
      <td>514329203</td>
      <td>288</td>
      <td>Streptomyces aurantiacus JA 4570</td>
      <td>None</td>
      <td>MAITALVSTAFTFQHAEAAGTGARVADQSTLAELKDARAEFDRRSS...</td>
      <td>gnl|WGS:AOPZ|STRAU_4813</td>
      <td>1286094</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>EXG79206.1</td>
      <td>trypsin-like serine protease with C-terminal P...</td>
      <td>589394449</td>
      <td>415</td>
      <td>Cryptosporangium arvum DSM 44712</td>
      <td>None</td>
      <td>MTTPRHRRSPTARRRNITISSVVAGAVAAALAAFMATAPTAGASDK...</td>
      <td>gnl|WGS:JFBT|CryarDRAFT_0234</td>
      <td>927661</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>WP_019676482.1</td>
      <td>S1 family peptidase [Rheinheimera perlucida]</td>
      <td>518506275</td>
      <td>503</td>
      <td>Rheinheimera perlucida</td>
      <td>None</td>
      <td>MKLIHVVVLFNAMKTFQISRLLLKIIMKKVINRKHFSCYKAFTYLA...</td>
      <td>NaN</td>
      <td>368811</td>
    </tr>
  </tbody>
</table>


## Install

Clone from source and install in development mode using pip.
```
git clone https://github.com/Zsailer/fetch_taxa
cd fetch_taxa
pip install -e .
```
