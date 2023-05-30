@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=../src
set BUILDDIR=../build

REM used for sphinx-apidoc
set APIDIR=api

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)
:sphinx_ok

if "%1" == "" goto help

if "%1" == "clean" (
	echo Cleaning up build and API directories
	if exist %BUILDDIR% rmdir /s /q %BUILDDIR%
	if exist %APIDIR% rmdir /s /q %APIDIR%
	goto end
)

if "%1" == "rst" (
	echo Creating RST files with sphinx-apidoc in %APIDIR%
		shpinx-apidoc -e -f -o %APIDIR% ../src
	goto end
)

if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
	goto end
)

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
