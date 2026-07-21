/**
 * api.js - Módulo para manejar las peticiones de datos
 */

const API = {

  basePath: "/MascotaDescifrada7",
  cache: {},

  async getPostsIndex() {
    if (this.cache.postsIndex) return this.cache.postsIndex;
    
    try {
      const response = await fetch(`${this.basePath}/data/posts-index.json`);
      if (!response.ok) throw new Error('Network response was not ok');
      const posts = await response.json();
      
      // Asegurar que siempre se muestren los más nuevos primero
      posts.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
      
      this.cache.postsIndex = posts;
      return this.cache.postsIndex;
    } catch (error) {
      console.error('Error fetching posts index:', error);
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

