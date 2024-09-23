import React from 'react';

const Loader = () => {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="w-16 h-16 border-4 border-solid border-gray-300 border-t-4 border-t-[#6AF41A] rounded-full animate-spin"></div>
    </div>
  );
};

export default Loader;
