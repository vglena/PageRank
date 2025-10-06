import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.
    """
    total_pages = len(corpus)
    probabilities = dict()

    links = corpus[page]
    if links:
        for p in corpus:
            probabilities[p] = (1 - damping_factor) / total_pages
            if p in links:
                probabilities[p] += damping_factor / len(links)
    else:
        # Page has no outgoing links, treat it as linking to all pages
        for p in corpus:
            probabilities[p] = 1 / total_pages

    return probabilities



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages.
    """
    page_rank = {page: 0 for page in corpus}
    pages = list(corpus.keys())

    # Start with a random page
    current_page = random.choice(pages)

    for _ in range(n):
        page_rank[current_page] += 1
        distribution = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(
            population=list(distribution.keys()),
            weights=list(distribution.values()),
            k=1
        )[0]

    # Normalize the ranks to sum to 1
    for page in page_rank:
        page_rank[page] /= n

    return page_rank



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iterative algorithm.
    """
    N = len(corpus)
    pagerank = {page: 1 / N for page in corpus}

    threshold = 0.001
    converged = False

    while not converged:
        new_rank = dict()
        for page in corpus:
            total = 0
            for possible_page in corpus:
                # Treat pages with no links as linking to all pages
                links = corpus[possible_page] or set(corpus.keys())
                if page in links:
                    total += pagerank[possible_page] / len(links)

            new_rank[page] = ((1 - damping_factor) / N) + (damping_factor * total)

        # Check convergence
        converged = all(abs(new_rank[page] - pagerank[page]) < threshold for page in corpus)
        pagerank = new_rank

    return pagerank



if __name__ == "__main__":
    main()
