# Inverse Laplace Transform Calculator

## Introduction

The Inverse Laplace Transform Calculator is a program that helps users classify and compute the inverse Laplace transform of a given function of $s$. This tool uses symbolic mathematics to identify different forms of Laplace-transformed functions and applies appropriate methods to solve for their inverse. It is suitable for mathematical, engineering, and physics applications where solving inverse Laplace transforms is necessary for analyzing time-domain behaviors.

The inverse Laplace transform $L^{-1} { F(s) }$ is commonly used to convert a function in the $s$-domain back to the $t$-domain.

## Classification Methods

This calculator classifies and solves Laplace transforms using the following methods:

### 1. Basic Transform
**Use When:** The function directly matches common Laplace transform pairs.
  
For example:
- $\frac{1}{s + a} \rightarrow e^{-at}$
- $\frac{s}{s^2 + 1} \rightarrow \cos(t)$

### 2. First Shifting Theorem
**Use When:** The function contains a term $e^{-a \cdot s}$.
  
**Formula:**
If $L\{ f(t) \} = F(s)$, then $L\{ f(t - a) \cdot u(t - a) \} = e^{-a \cdot s} \cdot F(s)$.

### 3. Partial Fraction Decomposition
**Use When:** The function is a rational expression and can be decomposed into simpler fractions.
  
For example:
- $\frac{s}{(s^2 + 4)(s^2 + 9)}$

### 4. Convolution
**Use When:** The function is a product of two simpler functions in the $s$-domain.
  
**Formula:**
$L^{-1} \{ F_1(s) \cdot F_2(s) \} = f_1(t) * f_2(t) = \int_0^t f_1(\tau) f_2(t - \tau) d\tau$

### 5. Differentiation in the $s$-domain
**Use When:** The function involves $s$-differentiation and requires time-domain differentiation.
  
For example:
- $L\{ t \cdot f(t) \} = -\frac{dF(s)}{ds}$

## Usage

### Beginner Installation

1. Install the requirements:
   ```bash
   pip install sympy
   ```
2. Run the program:
   ```bash
   python laplace_calculator.py
   ```

### Command-Line Arguments

- **Without Unicode Symbols**: Run with the `--no-unicode` flag if Unicode symbols are not supported in your environment.
  
  ```bash
  python laplace_calculator.py --no-unicode
  ```

### Input

Upon running, the program will prompt you to enter a function $F(s)$ in terms of $s$. It accepts standard arithmetic expressions using `s` as the variable, such as:

```plaintext
(s**2 + 16*s - 24) / (s**4 + 20*s**2 + 64)
```

### Output

The program will display:
1. The entered function in a formatted manner.
2. The solution for $L^{-1} \{ F(s) \}$, if classified successfully.

**Note**: If the function does not match any recognized classifications, the program will return an error message.

### Sample Run

```plaintext
Enter the Laplace function of s: (s**2 + 16 * s - 24) / (s**4 + 20 * s**2 + 64)
Entered equation:
   2
s  + 16⋅s - 24
───────────────
  4       2
s  + 20⋅s  + 64
Solution:
  7⋅sin(2⋅t)   5⋅sin(4⋅t)   4⋅cos(2⋅t)   4⋅cos(4⋅t)
- ────────── + ────────── + ────────── - ──────────
      6            6            3            3
```

