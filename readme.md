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

<p align="center">Voir le code dans le fichier main pour une meilleure présentation<p>
<p>
----------- Installation de la librairie rich
 
    # Dans le terminal

>   <code> pip install rich </code>

    # Affiche les fonctionnalités de la librairie

>   <code> python -m rich </code>

----------- Importation des fonctionnalités
 
    # Importe les fonctionnalités

<code>
from rich import print<br/>
from rich.table import Table<br/>
from rich.console import Console<br/>
from rich.progress import track<br/>
import time
</code>

----------- Fonctionnalité du print

    # ecrire en gras

<code>
print("[bold]Ce que je veux)"<br/>
</code>

    # écrire rouge sur blanc

<code>
print("[red on white]plein de cadeau")<br/>
</ode>

    # écrire une partie seulement rouge sur blanc

<code>
print("[red on white]plein[/] de cadeau")<br/>
</code>

----------- Faire un tableau

    # Titre du tableau

<code>
table = Table(title="Tableau de test")<br/>
</code>

    # Colonnes

<code>
table.add_column("Colonne1", style="cyan")<br/>
table.add_column("Colonne2", style="magenta")<br/>
table.add_column("Colonne3", style="white")<br/>
table.add_column("Colonne4", style="white")<br/>
</code>

    # lignes

<code>
table.add_row("info1", "info2", "info3", "info4")<br/>
table.add_row("info1", "info2", "info3", "info4")<br/>
table.add_row("info1", "info2", "info3", "info4")<br/>
table.add_row("info1", "info2", "info3", "info4")<br/>
</code>

    # Affichage du tableau

<code>
console = Console()<br/>
console.print(table)<br/>
</code>

----------- Faire une barre de progression

<code>
for i in track(range(100), description= "Chargement en cours"):<br/>
    time.sleep(0.1)
</code>
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
