using Test

@testset "Chapter initialization" begin
    include(joinpath(@__DIR__, "..", "..", "StartMe.jl"))
    @test isdir(DIR_RESULTS)
    @test isdir(DIR_FIGURES_SVG)
    @test isdir(DIR_FIGURES_PNG)
end
