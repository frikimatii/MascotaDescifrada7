/**
 * app.js - Controlador principal de la aplicación
 */
import API from './api.js';
import Render from './render.js';
import Search from './search.js';
import SEO from './seo.js';

const App = {
  async init() {
    Search.init();
    
    const path = window.location.pathname;
    
    // Load common Sidebar if exists
    await this.loadSidebar();

    if (path.includes('articulo.html')) {
      await this.loadArticlePage();
    } else if (path.includes('categoria.html')) {
      await this.loadCategoryPage();
    } else if (path.includes('buscar.html')) {
      await this.loadSearchPage();
    } else {
      // Assuming index.html or root
      await this.loadHomePage();
    }
  },

  async loadSidebar() {
    const sidebarContainer = document.getElementById('sidebar-container');
    if (!sidebarContainer) return;

    const posts = await API.getPostsIndex();
    const categories = await API.getCategories();
    sidebarContainer.innerHTML = Render.sidebar(posts, categories);
  },

  async loadHomePage() {
    const postsContainer = document.getElementById('latest-posts');
    if (!postsContainer) return;

    const posts = await API.getPostsIndex();
    postsContainer.innerHTML = posts.map(post => Render.postCard(post)).join('');
    
    const categoriesContainer = document.getElementById('home-categories');
    if (categoriesContainer) {
      const categories = await API.getCategories();
      categoriesContainer.innerHTML = categories.map(cat => Render.categoryPill(cat)).join('');
    }
  },

  async loadArticlePage() {
    const urlParams = new URLSearchParams(window.location.search);
    const slug = urlParams.get('slug');
    
    if (!slug) {
      window.location.href = '404.html';
      return;
    }

    const post = await API.getPostBySlug(slug);
    if (!post) {
      window.location.href = '404.html';
      return;
    }

    // Update SEO
    SEO.updateMeta(post.titulo, post.descripcion, post.imagen, window.location.href);

    // Render Article
    const contentContainer = document.getElementById('article-content');
    if (contentContainer) {
      let amazonHtml = '';
      if (post.productosAmazon && post.productosAmazon.length > 0) {
        amazonHtml = `<h3>Productos Recomendados</h3>` + post.productosAmazon.map(p => Render.amazonProduct(p)).join('');
      }

      contentContainer.innerHTML = `
        <div class="article-header">
          <a href="categoria.html?cat=${encodeURIComponent(post.categoria)}" class="category-pill" style="display:inline-block; margin-bottom:1rem;">${post.categoria}</a>
          <h1 style="font-size: 2.5rem;">${post.titulo}</h1>
          <div class="article-meta">
            <span>📅 ${post.fecha}</span>
            <span>⏱️ ${post.tiempoLectura}</span>
            <span>✍️ ${post.autor}</span>
          </div>
          <img src="${post.imagen}" alt="${post.titulo}" style="width:100%; border-radius:var(--radius-lg); margin-top:1rem; max-height:400px; object-fit:cover;">
        </div>
        <div class="article-content" style="font-size: 1.1rem; line-height: 1.8;">
          ${post.contenido}
          <div style="margin-top: 2rem;">
            ${amazonHtml}
          </div>
        </div>
      `;
    }
  },

  async loadCategoryPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const catName = urlParams.get('cat');
    const titleEl = document.getElementById('category-title');
    const container = document.getElementById('category-posts');
    
    if (!catName || !titleEl || !container) return;
    
    titleEl.textContent = `Categoría: ${catName}`;
    SEO.updateMeta(`Categoría: ${catName}`, `Artículos sobre ${catName}`, '', window.location.href);
    
    const posts = await API.getPostsIndex();
    const filtered = posts.filter(p => p.categoria === catName);
    
    if(filtered.length === 0){
      container.innerHTML = '<p>No hay artículos en esta categoría aún.</p>';
      return;
    }
    
    container.innerHTML = filtered.map(post => Render.postCard(post)).join('');
  },

  async loadSearchPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    const titleEl = document.getElementById('search-title');
    const container = document.getElementById('search-results');
    
    if (!query || !titleEl || !container) return;
    
    titleEl.textContent = `Resultados para: "${query}"`;
    SEO.updateMeta(`Buscar: ${query}`, `Resultados de búsqueda para ${query}`, '', window.location.href);

    const results = await Search.performSearch(query);
    
    if(results.length === 0){
      container.innerHTML = '<p>No se encontraron resultados. Intenta con otra palabra.</p>';
      return;
    }
    
    container.innerHTML = results.map(post => Render.postCard(post)).join('');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
