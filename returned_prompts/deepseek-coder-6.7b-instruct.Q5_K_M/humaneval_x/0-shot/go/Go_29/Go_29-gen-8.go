
	result := make([]string, 0)

	for _, v := range strings {
		if strings.HasPrefix(v, prefix) {
			result = append(result, v)
		}
	}

	return result
}

*/

package main

import (
	"fmt"
	"strings"
)

func FilterByPrefix(strings []string, prefix string) []string {

	result :

	make([]string, 0)

	for _, v := range strings {
		if strings.HasPrefix(v, prefix) {
			result = append(result, v)
		}
	}

	return result
}

func main() {

	fmt.Println(FilterByPrefix([]string{}, "a"))

	fmt.Println(FilterByPrefix([]string{"abc", "bcd", "cde", "array"}, "a"))
}
package main

import (
	"context"
	"fmt"
	"io"
	"os"
	"os/exec"
	"strings"
	"time"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
)

type DockerInfo struct {
	ContainerId string
	Image       string
	Command     string
	Created     int64
	Status      string
	Ports       string
	Names       string
}

func main() {
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

	containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{All: true})
	if err != nil {
		panic(err)
	}

	dockerInfos := make([]DockerInfo, 0)

	for _, container := range containers {
		containerId := container.ID
		image := container.Image
		command := container.Command
		created := container.Created
		status := container.Status
		ports := container.Ports
		names := container.Names

		