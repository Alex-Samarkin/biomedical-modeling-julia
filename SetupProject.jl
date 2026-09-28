using Pkg

Pkg.activate(".")
Pkg.add([
    "DifferentialEquations",
    "OrdinaryDiffEq",
    "ModelingToolkit",
    "DataFrames",
    "CSV",
    "Distributions",
    "StatsBase",
    "CairoMakie",
    "LaTeXStrings",
    "Pluto",
    "Test",
    "Plots",
    "PlotThemes",
    "JLD2",
    "JSON",
    "XLSX",
    "IJulia",
])
Pkg.status()