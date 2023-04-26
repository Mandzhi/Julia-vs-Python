using Pkg
Pkg.add("DataFrames")
Pkg.add("CSV")
Pkg.add("BenchmarkTools")
Pkg.add("Plots")

using DataFrames
# Create DataFrame
df = DataFrame(day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
              calories_burnt = [198, 324, 275, 346, 126, 146, 63],
              time_min = [20, 30, 30, 32, 10, 13, 5],
              weather = ["sunny", "sunny", "sunny", "sunny", "rainy", "gloomy", "rainy"]
              )
println(df)

# Sorting DataFrame
#df_sort = sort(df, "time_min")
#println(df_sort)
df_sort = sort(df, "time_min", rev=true)
println(df_sort)

# Filter to shorter runs
df_short = filter(row -> row.time_min<=20, df)
println(df_short)

# Make a Plot
using Plots

bar(df.day, df.time_min, legend = :none)
annotate!(df.day, df.time_min, df.time_min, :bottom)
ylabel!("Spent time (in minutes)")
xlabel!("Days")
savefig("plot.png")

# Reading a CSV file
using CSV
using DataFrames
using BenchmarkTools
#function read_csv:
data = CSV.read("Significant_Earthquakes.csv", DataFrame)
#println(df)
@btime CSV.read("Significant_Earthquakes.csv", DataFrame)
#@time CSV.read("Significant_Earthquakes.csv", DataFrame)
#@time CSV.read("Significant_Earthquakes.csv", DataFrame)


