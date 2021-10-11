io.write("101010101")
a = io.read("*a")

function love.draw()
    love.graphics.print(a,30)
end