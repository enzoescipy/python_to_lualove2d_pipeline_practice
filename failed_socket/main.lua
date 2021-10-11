-- load namespace
local socket = require("socket")
-- create a TCP socket and bind it to the local host, at any port
local server = assert(socket.bind("*", 0))
-- find out which port the OS chose for us
local ip, port = server:getsockname()

local f = io.open("hostinfo.txt","w")
f:write(ip.."\n"..port)
f:close()

-- print a message informing what's up
print("Please telnet to localhost on port " .. port)

local received = nil
-- loop forever waiting for clients
while true do
  local client = server:accept()
  print("Connected with the client")
  local line, err, partial = client:receive()
  print(line,err,partial)
  received = partial
  if not err then client:send(line .. "\n") end
  client:close()
  break
end

function love.draw()
  love.graphics.print(received)
end