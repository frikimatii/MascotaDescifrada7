/**
 * api.js - Módulo para manejar las peticiones de datos
 */

const ANIMAL_TYPES = {
  Perros: ['perros'],
  Gatos: ['gatos'],
  Conejos: ['conejos'],
  Hámsters: ['hámster', 'hámsters'],
};

const NAV_ORDER = ['Perros', 'Gatos', 'Conejos', 'Hámsters', 'Aves', 'Reptiles', 'Peces'];

const TOPIC_ORDER = ['Comportamiento', 'Salud', 'Alimentación', 'Cuidados', 'Perros', 'Hámsters'];

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


  postMatchesAnimal(post, animalLabel) {
    const tags = ANIMAL_TYPES[animalLabel];
    if (!tags || !post.tags) return false;
    return post.tags.some(tag => tags.includes(tag.toLowerCase()));
  },

  async getNavCategories() {
    const posts = await this.getPostsIndex();
    return NAV_ORDER.filter(label =>
      posts.some(post => this.postMatchesAnimal(post, label))
    );
  },

  filterPostsByCategory(catName, posts) {
    if (ANIMAL_TYPES[catName]) {
      return posts.filter(post => this.postMatchesAnimal(post, catName));
    }
    return posts.filter(post => post.categoria === catName);
  },

  async getCategories() {
    const posts = await this.getPostsIndex();
    const categories = [...new Set(posts.map(post => post.categoria))];

    return categories.sort((a, b) => {
      const indexA = TOPIC_ORDER.indexOf(a);
      const indexB = TOPIC_ORDER.indexOf(b);
      if (indexA === -1 && indexB === -1) return a.localeCompare(b, 'es');
      if (indexA === -1) return 1;
      if (indexB === -1) return -1;
      return indexA - indexB;
    });
  }

};


export default API;

