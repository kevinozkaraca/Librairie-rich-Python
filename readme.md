### Fonctionnalités de base pour la librairie rich

<p align="center">La librairie rich est une librairie qui permet de personnaliser son terminal<p>
<br/>
<p align="center">
  <img align="center" width="80%" alt="commande python -m rich" src="image1.png"/>
</p>
<br/>
<p align="center">Voici un exemple de ce que l'on peut réaliser<p>
<br/>
<p align="center">
  <img align="center" width="80%" alt="exemple de présentation" src="image2.png"/>
</p>
<br/>
<p>
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

    # Titre du tableau

table = Table(title="Tableau de test")

    # Colonnes

table.add_column("Colonne1", style="cyan")
table.add_column("Colonne2", style="magenta")
table.add_column("Colonne3", style="white")
table.add_column("Colonne4", style="white")

    # lignes

table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")
table.add_row("info1", "info2", "info3", "info4")

    # Affichage du tableau

console = Console()
console.print(table)

----------- Faire une barre de progression

for i in track(range(100), description= "Chargement en cours"):
    time.sleep(0.1)
</p>

### Mes reseaux sociaux : 

<p align="center">
  <br/>
    <div class="socialIcons">
            <a href="https://github.com/kevinozkaraca" target="_blank"><img width="5%" src="iconGithub.png" alt="Icone Github de Kevin Özkaraca" aria-label="Accedez à mes dépots Github" title="Accedez à mes dépots Github"></a>
            <a href="https://www.facebook.com/kevinozkaraca" target="_blank"><img width="5%" src="iconFacebook.png" alt="Icone Facebook de Kevin Özkaraca" aria-label="Accedez à mon compte Facebook" title="Accedez à mon compte Facebook" ></a>
             <a href="https://pinterest.com/kevinozkaraca" target="_blank"><img width="5%" src="iconPinterest.png" alt="Icone Pinterest de Kevin Özkaraca" aria-label="Accedez à mon compte Pinterest" title="Accedez à mon compte Pinterest"></a>
            <a href="https://twitter.com/kevinozkaraca" target="_blank"><img width="5%" src="iconTwitter.png" alt="Icone Twitter de Kevin Özkaraca" aria-label="Accedez à mon compte Twitter" title="Accedez à mon compte Twitter"></a>
            <a href="https://instagram.com/kevinozkaraca" target="_blank"><img width="5%" src="iconInstagram.png" alt="Icone Instagram de Kevin Özkaraca" aria-label="Accedez à mon compte Twitter" title="Accedez à mon compte Twitter"></a>
            <a href="https://www.linkedin.com/in/kevin-%C3%B6zkaraca-66a256209/" target="_blank"><img width="5%" src="iconLinkedin.png" alt="Icone Linkedin de Kevin Özkaraca" aria-label="Accedez à mon  compte Linkedin" title="Accedez à mon  compte Linkedin"></a>
            <a href="https://www.youtube.com/channel/UCgrJrS7eEZ-HpdyA6YoXRmw" target="_blank"><img width="5%" src="iconYoutube.png" alt="Icone Youtube de Kevin Özkaraca" aria-label="Accedez à ma chaine Youtube" title="Accedez à ma chaine Youtube"></a>
            <a href="mailto:kevin.ozkaraca@gmail.com" target="_blank"><img width="5%" src="iconGmail.png" alt="Icone Gmail de Kevin Özkaraca" aria-label="Envoyez moi un mail sur mon Gmail" title="Envoyez moi un mail sur mon Gmail" ></a>
    </div>  
</p>
