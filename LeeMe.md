Funcion para mos trar nuestro tree:
    function Show-Tree {
    param([string]$Path = ".", [int]$Depth = 2, [int]$CurrentLevel = 0)
    if ($CurrentLevel -gt $Depth) { return }
    $indent = "  " * $CurrentLevel
    Get-ChildItem -Path $Path -Directory | ForEach-Object {
        Write-Output "$indent+-- $($_.Name)"
        Show-Tree -Path $_.FullName -Depth $Depth -CurrentLevel ($CurrentLevel + 1)
    }
}
------------------------------------------------------------
git status
git add .
git commit -m "..."
git push

git pull

# APARTIR DEL 24/02/2026 NO SUBIREMOS LO QUE SE ENCUENTRE EN LA CARPETA DATA
# Ejecutar desde el directorio actual, mostrando hasta 2 niveles
Show-Tree -Depth 2   

# Recursos:
    Bootstrap: https://getbootstrap.com/
    FonsoneW:  https://fontawesome.com/

# MODIFICACIONES
##  18/02/2026
### Modificacion del titulo solo una vez Gestió d'espais publics
### Toquecito a los botones
### Excel semanal
##  19/02/2026
### Modificacion Agregamos campo en excel CLAUS de llaves actuales...
### Excel claus en tabla nuevo campo.
##  21/02/2026
### Retoques a los titulos.
##  22/02/2026
### Rectificació d'horaris.
## 24/02/2026
### Ultimos ficheros de datos y actualizacion de leeme.
### Rectificacion del gitIgnore data/*.xlsx *.csv
