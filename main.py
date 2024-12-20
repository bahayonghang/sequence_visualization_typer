import typer
from pathlib import Path
from plotter import plot_npy_all_train, plot_npy_all

app = typer.Typer()

@app.command()
def visualize():
    """
    Visualize the results.
    """
    try:
        type = typer.prompt("Please enter the type of visualization ('train' or 'test')")
        if type not in ["train", "test"]:
            raise ValueError("Invalid type. Please use 'train' or 'test'.")

        path = typer.prompt("Please enter the absolute path to the result directory")
        path = Path(path)
        if not path.is_absolute():
            raise ValueError("The path must be an absolute path.")
        if not path.exists():
            raise FileNotFoundError(f"The path {path} does not exist.")

        if type == "train":
            plot_npy_all_train(path)
        elif type == "test":
            plot_npy_all(path)
    except ValueError as ve:
        typer.echo(f"Error: {ve}")
    except FileNotFoundError as fnfe:
        typer.echo(f"Error: {fnfe}")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()