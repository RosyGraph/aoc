t = 0
flag = true
boards = Vector{Matrix{Int}}(nothing)
drawings = nothing
for line in eachline("in/1.in")
	if flag
		global drawings = [parse(Int, s) for s in split(line, ",")]
		global flag = false
	end
end
println(drawings)
