# === CONFIGURATION ===

$taskName = "UpdateNaukriResume"

$pythonPath = "C:\Path\To\python.exe"                  # 🔁 Replace with the path to python.exe

$scriptPath = "C:\Path\To\YourScript.py"               # 🔁 Replace with your Python script path

$morningTime = "08:00"                                 # 🔁 Morning time (e.g., 8 AM)

$eveningTime = "20:00"                                 # 🔁 Evening time (e.g., 8 PM)



# === BUILD ACTION ===

$action = New-ScheduledTaskAction -Execute $pythonPath -Argument ""$scriptPath""



# === BUILD TRIGGERS ===

$triggerMorning = New-ScheduledTaskTrigger -Daily -At $morningTime

$triggerEvening = New-ScheduledTaskTrigger -Daily -At $eveningTime



# === SETTINGS ===

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable



# === REGISTER TASK ===

Register-ScheduledTask `

    -TaskName $taskName `

    -Action $action `

    -Trigger @($triggerMorning, $triggerEvening) `

    -Settings $settings `

    -Description "Auto-upload resume to Naukri (morning & evening)" `

    -User "$env:USERNAME" `

    -RunLevel Highest `

    -Force



Write-Host "✅ Task '$taskName' created to run at $morningTime and $eveningTime daily."