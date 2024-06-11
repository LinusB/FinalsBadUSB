try {
    $Email = (Get-WmiObject -Query "SELECT * FROM Win32_UserAccount WHERE Name='$env:USERNAME'").Caption
    if ($Email) {
        Add-Content -Path .\user_info.txt -Value "Email: $Email"
    } else {
        Add-Content -Path .\user_info.txt -Value "Email: N/A"
    }
} catch {
    Add-Content -Path .\user_info.txt -Value "Email: N/A"
    Add-Content -Path .\user_info.txt -Value "Error: $_"
}
