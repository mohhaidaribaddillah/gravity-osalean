# PowerShell script to replace Material Symbols with Bootstrap Icons

$files = @(
    "invoice.html",
    "products.html",
    "blog.html"
)

$replacements = @{
    'href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@100..700,0..1&display=swap"' = 'href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"'
    '<span class="material-symbols-outlined text-[20px]">notifications</span>' = '<i class="bi bi-bell text-[20px]"></i>'
    '<span class="material-symbols-outlined text-[20px]">settings</span>' = '<i class="bi bi-gear text-[20px]"></i>'
    '<span class="material-symbols-outlined text-[24px]">menu</span>' = '<i class="bi bi-list text-[24px]"></i>'
    '<span class="material-symbols-outlined">close</span>' = '<i class="bi bi-x-lg"></i>'
    '<span class="material-symbols-outlined">dashboard</span>' = '<i class="bi bi-speedometer2"></i>'
    '<span class="material-symbols-outlined">analytics</span>' = '<i class="bi bi-graph-up"></i>'
    '<span class="material-symbols-outlined">receipt_long</span>' = '<i class="bi bi-receipt"></i>'
    '<span class="material-symbols-outlined">inventory_2</span>' = '<i class="bi bi-box-seam"></i>'
    '<span class="material-symbols-outlined">article</span>' = '<i class="bi bi-file-text"></i>'
    '<span class="material-symbols-outlined text-lg">add</span>' = '<i class="bi bi-plus-lg text-lg"></i>'
    '<span class="material-symbols-outlined text-lg">visibility</span>' = '<i class="bi bi-eye text-lg"></i>'
    '<span class="material-symbols-outlined text-lg">download</span>' = '<i class="bi bi-download text-lg"></i>'
    '<span class="material-symbols-outlined text-lg">send</span>' = '<i class="bi bi-send text-lg"></i>'
    '<span class="material-symbols-outlined text-sm mr-1">check_circle</span>' = '<i class="bi bi-check-circle text-sm mr-1"></i>'
    '<span class="material-symbols-outlined text-sm mr-1">schedule</span>' = '<i class="bi bi-clock text-sm mr-1"></i>'
    '<span class="material-symbols-outlined text-sm mr-1">error</span>' = '<i class="bi bi-exclamation-circle text-sm mr-1"></i>'
    '<span class="material-symbols-outlined">check_circle</span>' = '<i class="bi bi-check-circle"></i>'
    '<span class="material-symbols-outlined">schedule</span>' = '<i class="bi bi-clock"></i>'
    '<span class="material-symbols-outlined">error</span>' = '<i class="bi bi-exclamation-circle"></i>'
    '<span class="material-symbols-outlined">chevron_left</span>' = '<i class="bi bi-chevron-left"></i>'
    '<span class="material-symbols-outlined">chevron_right</span>' = '<i class="bi bi-chevron-right"></i>'
    '<span class="material-symbols-outlined text-2xl">arrow_upward</span>' = '<i class="bi bi-arrow-up text-2xl"></i>'
    '<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-[#61896f]">search</span>' = '<i class="bi bi-search absolute left-3 top-1/2 -translate-y-1/2 text-[#61896f]"></i>'
    '<span class="material-symbols-outlined text-lg">favorite_border</span>' = '<i class="bi bi-heart text-lg"></i>'
    '<span class="material-symbols-outlined text-sm">star</span>' = '<i class="bi bi-star-fill text-sm"></i>'
    '<span class="material-symbols-outlined">expand_more</span>' = '<i class="bi bi-chevron-down"></i>'
    '<span class="material-symbols-outlined text-lg">grid_view</span>' = '<i class="bi bi-grid-3x3-gap text-lg"></i>'
    '<span class="material-symbols-outlined text-lg">view_list</span>' = '<i class="bi bi-list-ul text-lg"></i>'
    '<span class="material-symbols-outlined text-lg">shopping_cart</span>' = '<i class="bi bi-cart text-lg"></i>'
}

foreach ($file in $files) {
    $filePath = Join-Path "c:\antygrafity\osalean-dashboard" $file
    
    if (Test-Path $filePath) {
        Write-Host "Processing $file..." -ForegroundColor Yellow
        
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        foreach ($key in $replacements.Keys) {
            $content = $content.Replace($key, $replacements[$key])
        }
        
        Set-Content $filePath -Value $content -Encoding UTF8 -NoNewline
        
        Write-Host "✓ Updated $file" -ForegroundColor Green
    } else {
        Write-Host "✗ File not found: $file" -ForegroundColor Red
    }
}

Write-Host "`n✅ All files updated successfully!" -ForegroundColor Green
