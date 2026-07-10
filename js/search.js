/**
 * search.js - Lógica de búsqueda
 */
import API from './api.js';

const Search = {
  async init() {
    const searchForm = document.getElementById('search-form');
    if (!searchForm) return;

    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = searchForm.querySelector('input').value;
      if (input.trim()) {
        window.location.href = `buscar.html?q=${encodeURIComponent(input.trim())}`;
      }
    });
  },

  async performSearch(query) {
    const posts = await API.getPostsIndex();
    const lowerQuery = query.toLowerCase();
    
    return posts.filter(post => {
      return (
        post.titulo.toLowerCase().includes(lowerQuery) ||
        post.descripcion.toLowerCase().includes(lowerQuery) ||
        post.categoria.toLowerCase().includes(lowerQuery) ||
        post.tags.some(tag => tag.toLowerCase().includes(lowerQuery))
      );
    });
  }
};

export default Search;
