param (
    [string]$action
)

# Get the root directory of the project
$rootDirectory = (Get-Item $PSScriptRoot).Parent.FullName
$subAction = $args[1]

# Change directory to the root of the project
Set-Location $rootDirectory

Write-Host "Root directory: $rootDirectory Action: $action SubAction: $subAction"

# if ($action -eq "--start") {
#     $subAction = $args[1]
    
#     if ($subAction -eq "frontend") {
#         # Change directory to the frontend directory
#         Set-Location "$rootDirectory\Frontend"
#         # Start frontend server
#         npm run start:frontend
#     }
#     elseif ($subAction -eq "backend") {
#         # Start backend server
#         uvicorn MMP:app --reload --port 8080
#     }
#     else {
#         Write-Host "Invalid argument. Usage: .\ControlApp.ps1 --start frontend OR .\ControlApp.ps1 --start backend"
#     }
# }
# else {
#     Write-Host "Invalid usage. Usage: .\ControlApp.ps1 --start frontend OR .\ControlApp.ps1 --start backend"
# }
