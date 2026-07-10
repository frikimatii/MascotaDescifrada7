/**
 * api.js - Módulo para manejar las peticiones de datos
 */

const API = {

  basePath: "/MascotaDescifrada7",

  async getPostsIndex() {
    try {

      const response = await fetch(
        `${this.basePath}/data/posts-index.json`
      );

      if (!response.ok) {
        throw new Error(
          `Error cargando posts-index.json: ${response.status}`
        );
      }

      return await response.json();

    } catch (error) {

      console.error(
        "Error fetching posts index:",
        error
      );

      return [];
    }
  },


  async getPostBySlug(slug) {

    try {

      const response = await fetch(
        `${this.basePath}/posts/${slug}.json`
      );


      if (!response.ok) {

        throw new Error(
          `Post no encontrado: ${slug}`
        );

      }


      return await response.json();


    } catch(error) {

      console.error(
        `Error fetching post ${slug}:`,
        error
      );

      return null;

    }

  },


  async getCategories(){

    const posts = await this.getPostsIndex();

    const categories = new Set(
      posts.map(post => post.categoria)
    );


    return Array.from(categories);

  }

};


export default API;

