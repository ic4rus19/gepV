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
# Ejecutar desde el directorio actual, mostrando hasta 2 niveles
Show-Tree -Depth 2   


Recursos:
    Bootstrap
    FonsoneW

    
