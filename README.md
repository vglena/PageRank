# 🌐 PageRank Calculator

This project implements the **PageRank algorithm**, a method for ranking web pages based on their link structure.  
The project includes two methods to compute PageRank:

1. **Sampling-based estimation** – Estimates PageRank using a random surfer model.  
2. **Iterative calculation** – Computes PageRank iteratively using the PageRank formula until convergence.

---

## 📖 Overview

Given a corpus of HTML pages, each page may link to other pages. The goal of the PageRank algorithm is to determine the importance of each page based on incoming links:

- Pages with more incoming links from important pages receive higher PageRank.  
- A **damping factor** simulates a random surfer who either follows a link from the current page or jumps to a random page.  

The project contains three main functions:

1. **transition_model(corpus, page, damping_factor)**  
   Returns a probability distribution over which page a random surfer would visit next.  
   - Follows links from `page` with probability `damping_factor`.  
   - With probability `1 - damping_factor`, jumps to any page in the corpus randomly.  
   - If `page` has no outgoing links, chooses randomly among all pages.

2. **sample_pagerank(corpus, damping_factor, n)**  
   Estimates PageRank values by generating `n` random samples.  
   - The first sample is a random page.  
   - Subsequent samples are drawn using the transition model from the previous sample.  
   - Returns a dictionary mapping each page to its estimated PageRank (sum = 1).

3. **iterate_pagerank(corpus, damping_factor)**  
   Computes PageRank iteratively until convergence:  
   - Initialize each page with rank 1 / N.  
   - Update ranks based on contributions from all linking pages.  
   - Pages with no links are treated as linking to all pages.  
   - Stops when all PageRank values change by less than 0.001 between iterations.  
   - Returns a dictionary mapping each page to its final PageRank (sum = 1).

---

## 🧩 File Structure

```text
pagerank/
│
├── pagerank.py          # Main program: implements transition_model, sample_pagerank, iterate_pagerank
├── corpus/              # Directory containing HTML files to analyze
├── requirements.txt     # Dependencies
├── LICENSE              # MIT License
└── README.md            # Documentation (this file)
```
## ▶️ Usage

1. Clone the repository:
```python
git clone https://github.com/yourusername/pagerank.git
cd pagerank
```
2. Install dependencies (if required):
```python
pip install -r requirements.txt
```
3. Run the PageRank program:
```python
python pagerank.py corpus
```
- `corpus` should be the path to a directory containing HTML files.
- The program outputs PageRank values computed by both sampling and iterative methods.
## 🧩 Dependencies / Requirements
- Python 3.8 or higher
- No third-party modules required by default
- Optionally, you can use numpy or pandas for additional processing (not required for core functionality)

Example `requirements.txt`:
```python
numpy>=1.21.0
pandas>=1.3.0
```
## 💡 Notes
- Damping factor is typically set to 0.85, simulating a random surfer.
- Number of samples affects the accuracy of the sampling method; default is 10,000.
- Both methods should produce similar PageRank results given the same corpus.

## 🏁 Credits
- Project inspired by CS50’s Introduction to Artificial Intelligence with Python (PageRank problem set).
- Designed for educational purposes to demonstrate probabilistic modeling and iterative algorithms.

## 📄 License
```text
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
