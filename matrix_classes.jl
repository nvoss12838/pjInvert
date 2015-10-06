abstract matrix

type G <: matrix
  # G matrix for holding greens functions
  G::Array{Float64}
end

type d <: matrix
  # data matrix for holding observations
  d::Vector{Float64}
end

type m <: matrix
  # model matrix with model paramaters
  m::Vector{Float64}
end