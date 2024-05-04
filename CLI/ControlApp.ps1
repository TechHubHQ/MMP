# Get the necessary paths
$home_dir = [Environment]::GetFolderPath("UserProfile")
$root_dir = Split-Path $PSScriptRoot -Parent
$cli_dir = Join-Path $root_dir "CLI"
$backend_dir = Join-Path $root_dir "Backend"
$frontend_dir = Join-Path $root_dir "Frontend"
$bat_dir = Join-Path $home_dir "AppData\Local\Microsoft\WindowsApps"

# Create the batch file with the alias if it doesn't exist
$batch_file_path = Join-Path $bat_dir "ControlApp.bat"
if (-not (Test-Path $batch_file_path)) {
    @"
@echo off
powershell.exe -ExecutionPolicy Bypass -File "$root_dir\CLI\ControlApp.ps1" %*
"@ | Out-File $batch_file_path -Encoding ASCII

    # Add the batch file to the system's PATH
    $env:Path += ";$bat_dir"
    [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User)
}

function Check-FrontendRunning {
    $frontend_process = Get-Process -Name "node" -ErrorAction SilentlyContinue
    return ($null -ne $frontend_process)
}

function Check-BackendRunning {
    $backend_process = Get-Process -Name "uvicorn" -ErrorAction SilentlyContinue
    $python_process = Get-Process -Name "python" -ErrorAction SilentlyContinue
    return ($null -ne $backend_process)
}

function Start-Frontend {
    if (Check-FrontendRunning) {
        Write-Host "Frontend is already running"
        return
    }

    Write-Host "---------------------- Invoking Frontend Start -----------------"
    Write-Host "Starting frontend..."
    Set-Location $frontend_dir
    Start-Process -FilePath "npm" -ArgumentList "run start:frontend" -NoNewWindow
    Write-Host "Frontend started successfully."
    Write-Host "---------------------- Frontend Start Done --------------------"
}

function Start-Backend {
    if (Check-BackendRunning) {
        Write-Host "Backend is already running"
        return
    }

    Write-Host "---------------------- Invoking Backend Start -----------------"
    Write-Host "Starting backend..."
    Set-Location $root_dir
    Start-Process -FilePath "uvicorn" -ArgumentList "MMP:app --reload" -NoNewWindow
    Write-Host "Backend started successfully."
    Write-Host "---------------------- Backend Start Done --------------------"
}

function Stop-Frontend {
    if (-not (Check-FrontendRunning)) {
        Write-Host "Frontend is not running"
        return
    }

    Write-Host "---------------------- Invoking Frontend Stop -----------------"
    Write-Host "Stopping frontend..."
    Get-Process -Name "node" | Stop-Process -Force
    Write-Host "Frontend stopped successfully."
    Write-Host "---------------------- Frontend Stop Done --------------------"
}

function Stop-Backend {
    $backend_process = Get-Process -Name "uvicorn" -ErrorAction SilentlyContinue
    if (-not $backend_process) {
        Write-Host "Backend is not running"
        return
    }

    Write-Host "---------------------- Invoking Backend Stop -----------------"
    Write-Host "Stopping backend..."
    $backend_process | Stop-Process -Force
    Write-Host "Backend stopped successfully."
    Write-Host "---------------------- Backend Stop Done --------------------"
}


function Restart-Frontend {
    Write-Host "---------------------- Invoking Frontend Restart -----------------"
    Write-Host "Restarting frontend..."
    Stop-Frontend
    Start-Frontend
    Write-Host "Frontend restarted successfully."
    Write-Host "---------------------- Frontend Restart Done --------------------"
}

function Restart-Backend {
    Write-Host "---------------------- Invoking Backend Restart -----------------"
    Write-Host "Restarting backend..."
    Stop-Backend
    Start-Backend
    Write-Host "Backend restarted successfully."
    Write-Host "---------------------- Backend Restart Done --------------------"
}

function Show-Help {
    Write-Host "----------------------------------- Show Usage -----------------------------------"
    Write-Host "Error: Invalid number of arguments."
    Write-Host "Usage: ControlApp.ps1 <command> <package>"
    Write-Host "Commands:"
    Write-Host "  --start frontend - Start the frontend"
    Write-Host "  --start backend - Start the backend"
    Write-Host "  --stop frontend - Stop the frontend"
    Write-Host "  --stop backend - Stop the backend"
    Write-Host "  --restart frontend - Restart the frontend"
    Write-Host "  --restart backend - Restart the backend"
    Write-Host "  --status frontend - Check frontend status"
    Write-Host "  --status backend - Check backend status"
    Write-Host "--------------------------------- Show Usage Done ---------------------------------"
}

# Parse command line arguments
$command = $args[0]
$package = $args[1]

switch ($command) {
    "--start" {
        switch ($package) {
            "frontend" { Start-Frontend }
            "backend" { Start-Backend }
            "all" { Start-Backend; Start-Frontend }
            default { Write-Host "Invalid package" }
        }
    }
    "--stop" {
        switch ($package) {
            "frontend" { Stop-Frontend }
            "backend" { Stop-Backend }
            "all" { Stop-Backend; Stop-Frontend }
            default { Write-Host "Invalid package" }
        }
    }
    "--restart" {
        switch ($package) {
            "frontend" { Restart-Frontend }
            "backend" { Restart-Backend }
            "all" { Restart-Backend; Restart-Frontend }
            default { Write-Host "Invalid package" }
        }
    }
    "--status" {
        switch ($package) {
            "frontend" { if (Check-FrontendRunning) { Write-Host "Frontend is running" } else { Write-Host "Frontend is not running" } }
            "backend" { if (Check-BackendRunning) { Write-Host "Backend is running" } else { Write-Host "Backend is not running" } }
            "all" {
                if (Check-FrontendRunning) { Write-Host "Frontend is running" } else { Write-Host "Frontend is not running" }
                if (Check-BackendRunning) { Write-Host "Backend is running" } else { Write-Host "Backend is not running" }
            }
            default { Write-Host "Invalid package" }
        }
    }
    "--help" { Show-Help }
    default { Write-Host "Invalid command or package" }
}
