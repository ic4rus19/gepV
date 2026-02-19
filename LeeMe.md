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


# Ejecutar desde el directorio actual, mostrando hasta 2 niveles
Show-Tree -Depth 2   

# Recursos:
    Bootstrap: https://getbootstrap.com/
    FonsoneW:  https://fontawesome.com/

# MODIFICACIONES
##  18/02/2025
### Modificacion del titulo solo una vez Gestió d'espais publics
### Toquecito a los botones
### Excel semanal
##  19/02/2025
### Modificacion Agregamos campo en excel CLAUS de llaves actuales...
### Excel claus en tabla nuevo campo.

