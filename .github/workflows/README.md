1. Create DockerHub personal access token
2. Create Github secret to store Dockerhub username and token
3. Create the GitHub Action Workflow in `techtrends-dockerhub.yml` file

As the next steps to your learning, maybe you can try setting custom tags instead of just latest. You can refer to this documentation and the below snippet: https://github.com/docker/metadata-action#tags-input. The metadata action will help you to push docker images with custom tags.

```
- name: Docker meta
        id: meta
        uses: docker/metadata-action@v3
        with:
          images: 
          tags: |
            type=sha
          flavor: |
            latest=true
- name: Build image and push
        uses: docker/build-push-action@v2
        with:
          context: 
          file: 
          platforms: 
          push: true
          tags: ${{ steps.meta.outputs.tags }}
```