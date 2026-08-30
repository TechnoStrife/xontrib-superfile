#!/usr/bin/env nix-shell
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          overlays = [ ];
          pkgs = import nixpkgs {
            inherit system overlays;
          };
        in
        {
          devShells.default = pkgs.mkShell {
            buildInputs = [
              (pkgs.python314.withPackages (python-pkgs: [
                python-pkgs.build
                python-pkgs.twine
              ]))
            ];
          };

          packages.default = pkgs.python314Packages.buildPythonPackage {
            pname = "xontrib-superfile";
            version = "0.0.2";
            pyproject = true;
            src = ./.;

            doCheck = false;

            build-system = with pkgs.python314Packages; [
              build
              xonsh
            ];

            meta = with pkgs.lib; {
              description = "[superfile](https://github.com/yorukot/superfile) support function in the [xonsh shell](https://xon.sh).";
              homepage = "https://github.com/TechnoStrife/xontrib-superfile";
              license = licenses.mit;
            };
          };
        }
      );
}
