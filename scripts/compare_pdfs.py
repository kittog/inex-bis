import camelot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import click

##### FUNCTIONS ########
def compare_df(df1, df2):
    comparison_df = df1.compare(df2).dropna(how='all').dropna(axis=1, how='all')
    if comparison_df.empty:
        print("Dataframes are identical.")
    else:
        sns.heatmap(comparison_df, cmap="coolwarm", center=0)
        plt.show()
    

def compare_tables(tables1, tables2):
    # compare tables
    if tables1.n != tables2.n:
        print("Number of tables in the two documents is different. \n")
        print(f"Tables in first document: {tables1.n} \n")
        print(f"Tables in second document: {tables2.n} \n")
        print("Please check the documents and try again.")
        return
    else:
        for i in range(tables1.n):
            # compare number of rows and columns
            if tables1[i].shape != tables2[i].shape:
                print(f"{tables1[i].shape} vs {tables2[i].shape} \n")
                print("Please check the tables and try again.")
                continue
            else:
                # compare content
                compare_df()


###### COMMAND LINE INTERFACE ######
@click.command()
@click.option('--pdf1', prompt="Enter first PDF filename to compare", help='First PDF file to compare')
@click.option('--pdf2', prompt="Enter second PDF filename to compare", help='Second PDF file to compare')
def pdf_files(pdf1, pdf2):
    click.echo(f"Comparing {pdf1} and {pdf2}...")
    return pdf1, pdf2

####### MAIN ########
def main():
    # open and read pdfs
    pdf1, pdf2 = pdf_files.main(standalone_mode=False)
    tables1 = camelot.read_pdf(f'{pdf1}', flavor="lattice", pages='1-end')
    tables2 = camelot.read_pdf(f'{pdf2}', flavor="lattice", pages='1-end')
    # compare tables
    compare_tables(tables1, tables2)

if __name__ == '__main__':
    main()