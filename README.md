
# Selenium Google Model

## Overview
In this repository, I've created a simple model of www.google.com and its sister sites using Selenium. There were three parts to this project: 
* Creating pre-determined automated flows to become familiar with Selenium's methods (ie running a simple Google search for "Cloudera"). These flows can be found in the directory `Starters`.
* Creating page object models for Google's homepage and sister pages to provide a layer between the hard-coded webpage code and the flows. These models can be found in the directory `page_objects`.
* Creating the tests, which can be found in the directory `tests` under `test_flows.py`.

## Models
Each page object contains a `locator_dictionary`, which tracks the location of important elements on the webpage. For example, on the Google homepage, its `locator_dictionary` might contain the XPath to the search bar. It also contains methods needed to interact with these elements, such as verification methods and getters/setters. 

## Tests
Using pytest, there are a number of tests in `test_flows.py` the that automate common flows and verify that the correct webpages are returned throughout the process. We can also pass in pre-determined exceptions to certain methods in the page objects to simulate how the test may respond to common errors (such as a NoSuchElementException). 
