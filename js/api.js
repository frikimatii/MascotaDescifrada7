/**
 * api.js - Módulo para manejar las peticiones de datos
 */

const API = {
  // Configuración de rutas relativas
  basePath: window.location.pathname.includes('/mascotas') ? '/mascotas' : '',
  cache: {
    postsIndex: null,
    posts: {}
  },
  
  async getPostsIndex() {
    if (this.cache.postsIndex) return this.cache.postsIndex;
    
    try {
      const response = await fetch(`${this.basePath}/data/posts-index.json`);
      if (!response.ok) throw new Error('Network response was not ok');
      this.cache.postsIndex = await response.json();
      return this.cache.postsIndex;
    } catch (error) {
      console.error('Error fetching posts index:', error);
      return [];
    }
  },

  async getPostBySlug(slug) {
    if (this.cache.posts[slug]) return this.cache.posts[slug];

    try {
      const response = await fetch(`${this.basePath}/posts/${slug}.json`);
      if (!response.ok) throw new Error('Post not found');
      this.cache.posts[slug] = await response.json();
      return this.cache.posts[slug];
    } catch (error) {
      console.error(`Error fetching post ${slug}:`, error);
      return null;
    }
  },
  
  async getCategories() {
    const posts = await this.getPostsIndex();
    const categories = new Set(posts.map(post => post.categoria));
    return Array.from(categories);
  }
};

export default API;
