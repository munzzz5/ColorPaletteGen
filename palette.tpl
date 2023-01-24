<!DOCTYPE html>
<html>
<head>
    <title>Color Palette</title>
    <style>
        .color-box {
            width: 100px;
            height: 100px;
            display: inline-block;
            
            float:left;
        }
    </style>
</head>
<body>
    % for hex_code in hex_codes:
        <div class="color-box" style="background-color: {{hex_code}};"></div>
    % end
</body>
</html>
