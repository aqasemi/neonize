set GOOS=windows
set GOARCH=amd64
set CGO_ENABLED=1
set CC=x86_64-w64-mingw32-gcc

protoc --go_out=. Neonize.proto def.proto
protoc --python_out=../proto --mypy_out=../proto def.proto Neonize.proto

python build.py

protoc --go_out=. --go-grpc_out=. -I . Neonize.proto def.proto

if exist defproto rmdir /s /q defproto
if exist github.com/aqasemi/neonize/defproto move github.com/aqasemi/neonize/defproto defproto
rmdir /s /q github.com

go build -buildmode=c-shared -ldflags=-s -o neonize.dll main.go
move /Y neonize.dll ..
