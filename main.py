import sys
from scripts.text_to_forms import infix_to_rnp
from scripts.table import create_table

def main():
    arg: str = sys.argv[1]
    try:
        rpn = infix_to_rnp(arg)
        create_table(rpn)
    except:
        print("invalid format")

if __name__ == "__main__":
    main()
