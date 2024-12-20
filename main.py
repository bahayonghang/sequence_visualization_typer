import typer
from pathlib import Path
from plotter import plot_npy_all_train, plot_npy_all

app = typer.Typer()

def visualize_once(type: str, path: Path):
    """
    Visualize the results once based on the type and path.
    """
    if type == "train":
        plot_npy_all_train(path)
    elif type == "test":
        plot_npy_all(path)
    else:
        typer.echo("Invalid type. Please use 'train' or 'test'.")

@app.command()
def visualize():
    """
    Visualize the results.
    """
    while True:
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

            while True:
                visualize_once(type, path)

                action = typer.prompt("Choose an action: continue, reset, exit")
                if action == "continue":
                    continue
                elif action == "reset":
                    break
                elif action == "exit":
                    return
                else:
                    typer.echo("Invalid action. Exiting.")
                    return
        except ValueError as ve:
            typer.echo(f"Error: {ve}")
            break
        except FileNotFoundError as fnfe:
            typer.echo(f"Error: {fnfe}")
            break
        except KeyboardInterrupt:
            typer.echo("\nOperation cancelled. Exiting.")
            break
        except Exception as e:
            typer.echo(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        typer.echo("\nOperation cancelled. Exiting.")
        