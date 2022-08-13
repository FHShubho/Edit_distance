# Edit Distance

> Edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another, that is measured by counting the minimum number of operations required to transform one string into the other



### DNA Edit Distance

###### Problem Statement

You all know that a DNA is a sequence of 4 nucleotides: A, T, C, G. Suppose you need to compute the “DNA distance” between two input DNA sequences. This distance is useful for measuring the biological similarity between two species. The DNA distance is exactly like edit distance except that –

(i)     the cost of deleting a nucleotide is always c1 (c1 is a user input),

(ii)    the cost of inserting a nucleotide is always c2 (c2 is a user input), and

(iii)  the cost of conversion from one nucleotide to another comes from a “cost matrix” (which is a user input).

In other words, in case of DNA distance, the substitution/deletion/insertion cost may not always be 1 – which was the case for ED. To illustrate, two sample DNA sequences X and Y as well as a sample cost matrix C is given below.

X = ATTGC

Y = GTAC

C:

|     | A   | T   | C   | G   |
| --- | --- | --- | --- | --- |
| A   | 0   | 1   | 3   | 4   |
| T   | 2   | 0   | 4   | 5   |
| C   | 2   | 3   | 0   | 1   |
| G   | 3   | 3   | 1   | 0   |

Here C[A,T] = 1 means to the cost (may represent biochemical cost) of substituting (i.e. converting to) A by T, is 1. On the other hand C[T,A] = 2 means the cost of substituting T by A is 2.

You have to write a program that reads (i) a cost matrix as well as (ii) two DNA sequences: X,Y, (iii) constant cost of insertion: c1, (iv) constant cost of deletion: c2. It then prints the DNA distance between X and Y. Your program should also print the minimal sequence of edit operations (no operation, substitute, insert, delete) required to convert X to Y.



###### Test Run

![](https://github.com/FHShubho/Edit_distance/blob/main/Snapshot/test_run.png)


