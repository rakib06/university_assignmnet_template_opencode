param(
    [Parameter(Mandatory=$true)]
    [string]$OutputPath
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms

$outputDirectory = Split-Path -Parent $OutputPath

if ($outputDirectory) {
    New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null
}

$screen = [System.Windows.Forms.Screen]::PrimaryScreen
$bounds = $screen.Bounds

$bitmap = New-Object System.Drawing.Bitmap(
    $bounds.Width,
    $bounds.Height,
    [System.Drawing.Imaging.PixelFormat]::Format32bppArgb
)

$graphics = [System.Drawing.Graphics]::FromImage($bitmap)

try {
    $graphics.CopyFromScreen(
        $bounds.Left,
        $bounds.Top,
        0,
        0,
        $bounds.Size
    )

    $bitmap.Save(
        $OutputPath,
        [System.Drawing.Imaging.ImageFormat]::Png
    )
}
finally {
    $graphics.Dispose()
    $bitmap.Dispose()
}

Write-Output "Screenshot saved to: $OutputPath"
