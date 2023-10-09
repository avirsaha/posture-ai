pyinstaller ^
--onedir ^
--name Sitfix_V_0-1-0-beta_x64_minimal ^
--add-data "..\..\src\judge.py;.\lib" ^
 --add-data "..\..\src\main.py;.\lib" ^
 --add-data "..\..\LICENSE.txt;." ^
 --add-data "..\..\imgs;.\assets" ^
 --specpath ".\build\build_config" ^
 --splash "..\..\imgs\SITFIX.png" ^
: --noconsole ^
: --add-binary "..\..\lib;.\lib" ^
--hidden-import=pyi_splash ^
 --icon "..\..\imgs\sitfixlogo.ico" ^
 src/app.py