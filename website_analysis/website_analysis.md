# Domain Name Analysis

This document serves as an analysis of the **National Center for Education Statistics (NCES)**. Here, I will break down the code of the website to create a domain name scraper to consolidate all the websites for further analysis.

## Context

I am basing this analysis on data from my local college, **Mott Community College**, located at:

**Address:**  
1401 E. Court St.  
Flint, MI 48503  

The most important information contained in this location is the **zip code** and the **state abbreviation (MI)**, both of which can be directly queried in the domain name. Take, for example, the following URL:

**Example URL:**  
`https://nces.ed.gov/collegenavigator/?s=MI&zc=48503&zd=50&of=3`

### Key Observations from the URL:
1. **Zip Code**:  
   Visible where `zc=48503`.

2. **State Abbreviation**:  
   Visible where `s=MI`.

3. **Radius**:  
   Visible where `zd=50`. This indicates the website is querying within a **50-mile radius**.

## Analysis Approach

These three pieces of information—**zip code, state abbreviation**, and **radius**—are critical for further analysis. They will guide the way I extract and analyze data from the domain.

---

# Initial HTML Analysis
There are filters in the broad picture where you can **sort by Name, City, State, and Distance.** These are not required to be analyzed within this Initial HTML query (as visible in `initial_search.png`) since I will analyze them on an individual webpage basis.

Each of the results are displayed in ```<div class="resultCon">```, then it further develops into:

```<table id="ct100_cphCollegeNavBody_ucResultsMain_tblResults" class="resultsTable">
<tbody>
<tr class="resultsW"> (or <tr class="resultsY"> depending on if the table is display odd or even to change color from white to yellow)
```

Then, it breaks itself down into **3 ```<td>``` Data Cells**, with the most important being the **info button**, which includes a lot of important information:

```
** Displays the image that is used for the user to hover over and view extra information about the University.
**

<td class="infobutton" scope="row">

<div class="infoimage" onmouseover="this.nextSibling.style.display='block';" onmouseout="this.nextSibling.style.display='none';"></div> 
```

```
**
Acts as a way to divide the individual information while hovering over the iPop icon.
**

<div class="iPop" style="display: none;">
```


**iPop** is divided into three extra ```<div>``` classes, however the most important one is ```<div class="iBack">``` since it contains and displays all of the information that is viewable about the University without clicking on the website.

## Initial HTML Analysis Recap
#### Information is divided into this hierarchy:

```
<div class="resultCon">
<table id="ct100_cphCollegeNavBody_ucResultsMain_tblResults" class="resultsTable">
<tbody>
<tr class="resultsW"> (or <tr class="resultsY">)
<td class="infobutton" scope="row">
<div class="infoimage" onmouseover="this.nextSibling.style.display='block';" onmouseout="this.nextSibling.style.display='none';"></div> 
<div class="iPop" style="display: none;">
<div class="iBack">
```

# Further HTML Analysis
After being recapped on the **Initial HTML Analysis**, it is time to dissect ```<div class="iBack">```.

For this example, I will be analyzing `Kettering University`.
Within ```<div class="iBack">```, you can find the following structure:

<hr>

```
<table class="iTables">
<tbody>
```

Within ```<tbody>```, you can find 10 ```<tr>``` rows containing the following information:

**Table Row 1:** Displays the University name in a ```<h2>``` tag and then the address of the University in the paragraph text format. 

```
<td class="pbe" scope="row" colspan="2"> <h2>Kettering University</h2>1700 University Avenue, Flint, Michigan 48504-6214</td>
```

**Table Row 2:** Displays the approximate distance from the queried ZIP code (in our case, 48503 is approximately 3.2 miles from Kettering University).

```
<tr><td scope="row" class="srb">Distance from ZIP:&nbsp;&nbsp;</td><td class="sra">3.2 miles&nbsp;from 48503</td></tr>
```

**Table Row 3:** Displays General Information, which usually includes the Phone Number for the school.

```
<tr><td scope="row" class="srb">General information:&nbsp;&nbsp;</td><td class="sra">(800) 955-4464</td></tr>
```

**Table Row 4:** Displays the type of University. For example, if the school only provides `Certificates`, then it would be considered **< 2-years, Public or Private, and finally followed by for-profit or non-profit.**

```
<tr><td scope="row" class="srb">Type:&nbsp;&nbsp;</td><td class="sra">4-year, Private not-for-profit</td></tr>
```

**Table Row 5:** Displays the Awards the University offers. For example, an Associate's Degree, a Bachelor's Degree, a Master's Degree, etc.

```
<tr><td scope="row" class="srb">Awards offered:&nbsp;&nbsp;</td><td class="sra">Bachelor's degree<br>Postbaccalaureate certificate<br>Master's degree</td></tr>
```

**Table Row 6:** Display the Campus Setting. This is fairly arbitrary, so it's not important for my section of the analysis, as I will be cross comparing my findings against various studies. For example, `Kettering University` has a Campus Setting of City: Small.

```
<tr><td scope="row" class="srb">Campus setting:&nbsp;&nbsp;</td><td class="sra">City: Small</td></tr>
```

**Table Row 7:** Displays whether or not the Campus has on-site housing. Simply defined as Yes or No.

```
<tr><td scope="row" class="srb">Campus housing:&nbsp;&nbsp;</td><td class="sra">Yes</td></tr>
```

**Table Row 8:** Displays the Student Population, as well as the how many of those students are Undergraduates.

```
<tr><td scope="row" class="srb">Student population:&nbsp;&nbsp;</td><td class="sra">1,605 (1,290 undergraduate)</td></tr>
```

**Table Row 9:** Display the Student-to-Faculty ratio. For example, `Kettering University` has a ratio of 11 to 1.

```
<tr><td scope="row" class="srb">Student-to-faculty ratio:&nbsp;&nbsp;</td><td class="sra">11 to 1</td></tr>
```

**Table Row 10:** Displays the **IPEDS ID** as well as the **OPE ID**.

The **Integrated Postsecondary Education Data System (IPEDS)** is a system of interrelated surveys conducted annually by the National Center for Education Statistics. The **IPEDS ID** is especially important for my analysis because it allows me to query all of the websites. For example, clicking on **Kettering University** allows me to see the following Domain: `https://nces.ed.gov/collegenavigator/?s=MI&zc=48503&zd=50&of=3&id=169983` where `id=169983` is the **IPEDS ID**.

**OPE ID** stands for ***The Office of Postsecondary Education Identification***. It is an eight-digit number assigned by the **U.S. Department of Education** (regardless of the Department of Education being shut down, this project will go on) to schools participating in Title IV programs.

```
<tr><td scope="row" colspan="2"><p class="ipeds hoverID">IPEDS ID: 169983&nbsp;|&nbsp;OPE ID:&nbsp;00226200</p></td></tr>
```