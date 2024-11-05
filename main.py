import sympy as sp
from sympy.printing.pretty import pretty
import argparse
import sys

# Define variables
s, t = sp.symbols('s t')

def classify_and_solve_laplace(F_s):
    """
    Classifies the given Laplace-transformed function and attempts to find its inverse Laplace transform.
    
    Parameters:
    F_s (sympy expression): The function in the Laplace domain.
    
    Returns:
    sympy expression or str: The inverse Laplace transform if classification succeeds, otherwise an error message.
    """
    # Classification and Solving
    if F_s.is_rational_function(s):
        # Check for basic transform
        basic_transforms = {
            1/(s + 1): sp.exp(-t),
            1/(s**2 + 1): sp.sin(t),
            s/(s**2 + 1): sp.cos(t),
            1/s: 1,
        }
        for f_s, inverse_f_t in basic_transforms.items():
            if sp.simplify(F_s - f_s) == 0:
                return inverse_f_t  # Return as expression
        
        # Check for First Shifting Property
        if F_s.has(sp.exp(-s * sp.Symbol('a'))):
            a = sp.Symbol('a')
            transformed = F_s.subs(sp.exp(-a * s), 1)
            return sp.exp(-a * t) * sp.inverse_laplace_transform(transformed, s, t)
        
        # Check for Partial Fractions
        if sp.apart(F_s, s) != F_s:
            decomposed = sp.apart(F_s, s)
            return sp.inverse_laplace_transform(decomposed, s, t)
        
        # Check for Differentiation
        if F_s.diff(s) != 0:
            differentiated = F_s * s
            return t * sp.inverse_laplace_transform(differentiated, s, t)
    
    # Check for Convolution
    if F_s.is_Mul:
        terms = F_s.as_ordered_factors()
        if len(terms) == 2:
            F1, F2 = terms
            inv_F1 = sp.inverse_laplace_transform(F1, s, t)
            inv_F2 = sp.inverse_laplace_transform(F2, s, t)
            tau = sp.Symbol('tau')
            convolution = sp.integrate(inv_F1.subs(t, tau) * inv_F2.subs(t, t - tau), (tau, 0, t))
            return convolution
    
    return "Unable to classify the function for Inverse Laplace Transform."

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Classifies and solves the inverse Laplace transform for a given function in terms of 's'.",
        epilog="Examples:\n"
               "  python script.py                # Run with Unicode symbols\n"
               "  python script.py --no-unicode   # Run without Unicode symbols",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--no-unicode", action="store_true",
        help="Disable Unicode symbols in output (use ASCII-only characters)."
    )
    args = parser.parse_args()
    
    # Set pretty print option
    use_unicode = not args.no_unicode
    
    # User input
    try:
        user_input = input("Enter the Laplace function of s: ")
        F_s = sp.sympify(user_input)
    except (sp.SympifyError, TypeError):
        print("Error: Invalid input for Laplace function.")
        sys.exit(1)

    # Display entered equation
    print("Entered equation:")
    print(pretty(F_s, use_unicode=use_unicode))

    # Classification and solution
    result = classify_and_solve_laplace(F_s)
    if isinstance(result, sp.Basic):  # Check if it's a sympy expression
        # Substitute Heaviside(t) with 1
        result = result.subs(sp.Heaviside(t), 1)

    print("Solution:")
    print(pretty(result, use_unicode=use_unicode))

if __name__ == "__main__":
    main()
