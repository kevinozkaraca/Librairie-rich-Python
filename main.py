from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import track
import time

presentation = '''
oooooooooo.   o8o                                                                                
`888'   `Y8b  `"'                                                                                
 888     888 oooo   .ooooo.  ooo. .oo.   oooo    ooo  .ooooo.  ooo. .oo.   oooo  oooo   .ooooo.  
 888oooo888' `888  d88' `88b `888P"Y88b   `88.  .8'  d88' `88b `888P"Y88b  `888  `888  d88' `88b 
 888    `88b  888  888ooo888  888   888    `88..8'   888ooo888  888   888   888   888  888ooo888 
 888    .88P  888  888    .o  888   888     `888'    888    .o  888   888   888   888  888    .o 
o888bood8P'  o888o `Y8bod8P' o888o o888o     `8'     `Y8bod8P' o888o o888o  `V88V"V8P' `Y8bod8P' '''

# Pour afficher un message de ce genre chercher : acsii art générator !
'''
----------- Installation de la librairie rich
 
    # Dans le terminal
>   pip install rich
    # Affiche les fonctionnalités de la librairie
>   python -m rich

----------- Importation des fonctionnalités
 
    # Importe les fonctionnalités
from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import track
import time

----------- Fonctionnalité du print

    # ecrire en gras
print("[bold]Ce que je veux)"
    # écrire rouge sur blanc
print("[red on white]plein de cadeau")
    # écrire une partie seulement rouge sur blanc
print("[red on white]plein[/] de cadeau")

----------- Faire un tableau

table = Table(title="Tableau de test")

table.add_column("Colonne1", style="cyan")
table.add_column("Colonne2", style="magenta")
table.add_column("Colonne3", style="white")
table.add_column("Colonne4", style="white")

table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")

table.add_row("info1", "info2", "info3", "info4")

console = Console()
console.print(table)

----------- Faire une barre de progression

for i in track(range(100), description= "Chargement en cours"):
    time.sleep(0.1)
'''


# Les exemples du print
print(presentation)

time.sleep(1)

print("[bold]Ce que je veux")
print("[red on white]plein de cadeaux")
print("[red on white]plein[/] de cadeaux")

time.sleep(1)

# Exemple de tableau

table = Table(title="Tableau de test")

table.add_column("Colonne1", style="cyan")
table.add_column("Colonne2", style="magenta")
table.add_column("Colonne3", style="yellow")
table.add_column("Colonne4", style="green")

table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")

table.add_row("info1", "info2", "info3", "info4")

console = Console()
console.print(table)

time.sleep(1)

# Exemple de barre de progression

for i in track(range(100), description= "Chargement en cours"):
    time.sleep(0.1)

time.sleep(1)

print("Fin du programme")